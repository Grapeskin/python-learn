# 数据监控

## EMQ规则引擎（数据拦截）
~~~
一、数据入口
规则1：采集主板设备数据(过滤掉雷达数据)
SELECT
  nth(3, tokens(topic,'/')) as sn,
  json_decode(payload.data) as data,
  data.Lidar2D as Lidar2D
FROM
  "/dev/jig/+/event/post"
WHERE
  is_null(Lidar2D)

规则2：采集治具设备数据
SELECT
  nth(3, tokens(topic,'/')) as sn,
  json_decode(payload.data) as data
FROM
  "/dev/jig/+/service/response"

二、数据出口(robot/jig)
1. 主板设备数据
topic  : /robot/event/monitor
payload:
{
    "sn": "${sn}",
    "data": ${data}
}
2. 治具设备数据
topic  : /jig/event/monitor
payload:
{
    "sn": "${sn}",
    "data": ${data}
}
~~~
## Telegraf（数据采集）
## 数据存储
~~~
一、数据入口(robot/jig)
topic1: /robot/event/monitor
topic2: /jig/event/monitor

二、出口
以sn为tag，属性值为field存储influxdb
// 采集配置
[[inputs.mqtt_consumer]]
  servers = ["tcp://192.168.160.45:1883"]
  topics = [
    "/robot/event/monitor"
  ]
  username = "telegraf"
  password = "12345678"

  data_format = "json_v2"
  [[inputs.mqtt_consumer.json_v2]]
      measurement_name = "robot_consumer"
      #timestamp_path = "timestamp"
      #timestamp_format = "unix_ms"
      [[inputs.mqtt_consumer.json_v2.object]]
          path = "@this"
          tags = ["sn"]
          disable_prepend_keys = true
[[inputs.mqtt_consumer]]
  servers = ["tcp://192.168.160.45:1883"]
  topics = [
    "/jig/event/monitor"
  ]
  username = "telegraf"
  password = "12345678"

  data_format = "json_v2"
  [[inputs.mqtt_consumer.json_v2]]
      measurement_name = "jig_consumer"
      #timestamp_path = "timestamp"
      #timestamp_format = "unix_ms"
      [[inputs.mqtt_consumer.json_v2.object]]
          path = "@this"
          tags = ["sn"]
          disable_prepend_keys = true
~~~

## 数据分析
### Grafana规则
~~~
1. 扫地机类型
// 动态过滤条件SN
import "influxdata/influxdb/schema"

schema.measurementTagValues(
    bucket: "example-bucket",
    measurement: "robot_consumer",
    tag: "sn",
)

// 动态过滤条件property
import "influxdata/influxdb/schema"

schema.measurementFieldKeys(
    bucket: "example-bucket",
    measurement: "robot_consumer",
    start: -30d,
)

// flux动态查询语句
from(bucket: "example-bucket")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["sn"] == "${SN}")
  |> filter(fn: (r) => contains(value: r["_field"], set: ${property:json}))
  |> toInt()
  |> drop(columns: ["topic", "_measurement", "sn"])

2. 治具类型
import "influxdata/influxdb/schema"

schema.measurementTagValues(
    bucket: "example-bucket",
    measurement: "jig_consumer",
    tag: "sn",
)

// 动态过滤条件property
import "influxdata/influxdb/schema"

schema.measurementFieldKeys(
    bucket: "example-bucket",
    measurement: "jig_consumer",
    start: -30d,
)

// flux动态查询语句
from(bucket: "example-bucket")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["sn"] == "${SN}")
  |> filter(fn: (r) => contains(value: r["_field"], set: ${property:json}))
  |> toInt()
  |> drop(columns: ["topic", "_measurement", "sn"])

~~~
### Grafana模板
~~~
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": "-- Grafana --",
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": 1,
  "iteration": 1650337684418,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 0
      },
      "id": 42,
      "panels": [],
      "title": "主板治具联调类",
      "type": "row"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 0,
        "y": 1
      },
      "id": 40,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "t1 = from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${JIG_SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"DI6\")\r\n\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n\r\nt2 = from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"PoleConnectStatus\")\r\n\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n\r\nunion(tables: [t1, t2])",
          "refId": "A"
        }
      ],
      "title": "集尘解码设备",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 8,
        "y": 1
      },
      "id": 32,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "t1 = from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${JIG_SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"AI1\" or r[\"_field\"] == \"AI2\" or r[\"_field\"] == \"EAI1\")\r\n\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n\r\nt2 = from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"BatteryLevel\")\r\n\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n\r\nunion(tables: [t1, t2])",
          "refId": "A"
        }
      ],
      "title": "电池设备组",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 16,
        "y": 1
      },
      "id": 34,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"LeftPickUp\" or r[\"_field\"] == \"RightPickUp\" or r[\"_field\"] == \"DustBoxStatus\" or r[\"_field\"] == \"CollisionLeft\" or r[\"_field\"] == \"CollisionRight\" or r[\"_field\"] == \"MopStatus\" or r[\"_field\"] == \"FindChargeButton\")\r\n\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])",
          "refId": "A"
        }
      ],
      "title": "按键设备组",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 0,
        "y": 9
      },
      "id": 38,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"IrLeft\" or r[\"_field\"] == \"IrRight\" or r[\"_field\"] == \"IrFrontRight\" or r[\"_field\"] == \"IrFrontLeft\" or r[\"_field\"] == \"IrBackRight\" or r[\"_field\"] == \"IrBackLeft\")\r\n\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])",
          "refId": "A"
        }
      ],
      "title": "红外解码设备组",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 8,
        "y": 9
      },
      "id": 36,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "t1 = from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"LedError\" or r[\"_field\"] == \"LedHome\" or r[\"_field\"] == \"LedPower\" or r[\"_field\"] == \"LedWifi\" or r[\"_field\"] == \"UvHardwareConfig\")\r\n\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n\r\nt2 = from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${JIG_SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"DI1\" or r[\"_field\"] == \"DI2\" or r[\"_field\"] == \"DI3\" or r[\"_field\"] == \"DI4\" or r[\"_field\"] == \"DI5\")\r\n\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n\r\nunion(tables: [t1, t2])",
          "refId": "A"
        }
      ],
      "title": "灯设备组",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 17
      },
      "id": 24,
      "panels": [],
      "repeat": "SN",
      "title": "电机组件类",
      "type": "row"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 0,
        "y": 18
      },
      "id": 16,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"WaterPumpCurrent\"\r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n\r\n",
          "refId": "A"
        }
      ],
      "title": "水泵电流数值监控",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 8,
        "y": 18
      },
      "id": 10,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"MidBroomCurrent\"\r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n",
          "refId": "A"
        }
      ],
      "title": "中刷电流数值监控",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 16,
        "y": 18
      },
      "id": 14,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"SideBroomCurrentL\" or r[\"_field\"] == \"SideBroomCurrentR\" \r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n",
          "refId": "A"
        }
      ],
      "title": "边刷电流数值监控",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 0,
        "y": 26
      },
      "id": 4,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"FanCurrent\" or r[\"_field\"] == \"FanSpeed\" \r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n\r\n",
          "refId": "A"
        }
      ],
      "title": "风机电机检测数值监控",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": [
          {
            "__systemRef": "hideSeriesFrom",
            "matcher": {
              "id": "byNames",
              "options": {
                "mode": "exclude",
                "names": [
                  "WheelCurrentL"
                ],
                "prefix": "All except:",
                "readOnly": true
              }
            },
            "properties": [
              {
                "id": "custom.hideFrom",
                "value": {
                  "legend": false,
                  "tooltip": false,
                  "viz": true
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 8,
        "y": 26
      },
      "id": 12,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"WheelCurrentL\" or r[\"_field\"] == \"LeftSpeed\" or r[\"_field\"] == \"WheelCurrentR\" or r[\"_field\"] == \"RightSpeed\" \r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n",
          "refId": "A"
        }
      ],
      "title": "主轮电流与转速数值监控",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 34
      },
      "id": 22,
      "panels": [],
      "repeat": "SN",
      "title": "传感器类",
      "type": "row"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 7,
        "w": 8,
        "x": 0,
        "y": 35
      },
      "id": 2,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"WallDistance0\" or r[\"_field\"] == \"WallDistance1\" \r\n\r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n",
          "refId": "A"
        }
      ],
      "title": "沿墙数值监控",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "decimals": 0,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 7,
        "w": 8,
        "x": 8,
        "y": 35
      },
      "id": 8,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"AcceX\" or r[\"_field\"] == \"AcceY\" or r[\"_field\"] == \"AcceZ\" or r[\"_field\"] == \"GyroX\" or r[\"_field\"] == \"GyroY\" or r[\"_field\"] == \"GyroZ\"\r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n\r\n",
          "refId": "A"
        }
      ],
      "title": "IMU数值监控",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": [
          {
            "__systemRef": "hideSeriesFrom",
            "matcher": {
              "id": "byNames",
              "options": {
                "mode": "exclude",
                "names": [
                  "Cliff4"
                ],
                "prefix": "All except:",
                "readOnly": true
              }
            },
            "properties": [
              {
                "id": "custom.hideFrom",
                "value": {
                  "legend": false,
                  "tooltip": false,
                  "viz": true
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 7,
        "w": 8,
        "x": 16,
        "y": 35
      },
      "id": 6,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"Cliff0\" or r[\"_field\"] == \"Cliff1\" or r[\"_field\"] == \"Cliff2\" or r[\"_field\"] == \"Cliff3\" or r[\"_field\"] == \"Cliff4\"  or r[\"_field\"] == \"Cliff5\" \r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n\r\n",
          "refId": "A"
        }
      ],
      "title": "地检数值监控",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 7,
        "w": 8,
        "x": 0,
        "y": 42
      },
      "id": 20,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"Ultrasonic0\"\r\n\r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n",
          "refId": "A"
        }
      ],
      "title": "超声波传感器数值",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 7,
        "w": 8,
        "x": 8,
        "y": 42
      },
      "id": 18,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"WallSensor0\" or r[\"_field\"] == \"WallSensor1\" or r[\"_field\"] == \"WallSensor2\"\r\n\r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n",
          "refId": "A"
        }
      ],
      "title": "墙检数值监控",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 7,
        "w": 8,
        "x": 16,
        "y": 42
      },
      "id": 26,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"MopStatus\"\r\n\r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n",
          "refId": "A"
        }
      ],
      "title": "拖布在位检测",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 7,
        "w": 8,
        "x": 0,
        "y": 49
      },
      "id": 28,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"IrCollision0\" or r[\"_field\"] == \"IrCollision1\"\r\n\r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n",
          "refId": "A"
        }
      ],
      "title": "红外碰撞传感器",
      "type": "timeseries"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 7,
        "w": 8,
        "x": 8,
        "y": 49
      },
      "id": 30,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "mC-ZYfL7z"
          },
          "query": "from(bucket: \"example-bucket\")\r\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\r\n  |> filter(fn: (r) => r[\"sn\"] == \"${SN}\")\r\n  |> filter(fn: (r) => r[\"_field\"] == \"IrAlongWall0\"\r\n\r\n   )\r\n  |> drop(columns: [\"topic\", \"_measurement\", \"sn\"])\r\n",
          "refId": "A"
        }
      ],
      "title": "红外沿墙传感器",
      "type": "timeseries"
    }
  ],
  "refresh": "5s",
  "schemaVersion": 34,
  "style": "dark",
  "tags": [],
  "templating": {
    "list": [
      {
        "current": {
          "selected": true,
          "text": "JGJPTWD0000000243B82F9FC",
          "value": "JGJPTWD0000000243B82F9FC"
        },
        "definition": "import \"influxdata/influxdb/schema\"\r\n\r\nschema.measurementTagValues(\r\n    bucket: \"example-bucket\",\r\n    measurement: \"robot_consumer\",\r\n    tag: \"sn\",\r\n)",
        "description": "扫地机SN",
        "hide": 0,
        "includeAll": false,
        "multi": false,
        "name": "SN",
        "options": [],
        "query": "import \"influxdata/influxdb/schema\"\r\n\r\nschema.measurementTagValues(\r\n    bucket: \"example-bucket\",\r\n    measurement: \"robot_consumer\",\r\n    tag: \"sn\",\r\n)",
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 1,
        "type": "query"
      },
      {
        "current": {
          "selected": true,
          "text": "JGJPMCK00000001220124004",
          "value": "JGJPMCK00000001220124004"
        },
        "definition": "import \"influxdata/influxdb/schema\"\r\n\r\nschema.measurementTagValues(\r\n    bucket: \"example-bucket\",\r\n    measurement: \"jig_consumer\",\r\n    tag: \"sn\",\r\n)",
        "description": "JIG_SN",
        "hide": 0,
        "includeAll": false,
        "multi": false,
        "name": "JIG_SN",
        "options": [],
        "query": "import \"influxdata/influxdb/schema\"\r\n\r\nschema.measurementTagValues(\r\n    bucket: \"example-bucket\",\r\n    measurement: \"jig_consumer\",\r\n    tag: \"sn\",\r\n)",
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 1,
        "type": "query"
      }
    ]
  },
  "time": {
    "from": "now-2m",
    "to": "now"
  },
  "timepicker": {
    "hidden": false,
    "refresh_intervals": [
      "5s",
      "10s",
      "30s",
      "1m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ],
    "time_options": [
      "5m",
      "15m",
      "1h",
      "6h",
      "12h",
      "24h",
      "2d",
      "7d",
      "30d"
    ],
    "type": "timepicker"
  },
  "timezone": "browser",
  "title": "扫地机状态面板",
  "uid": "9yd-hEYnz",
  "version": 29,
  "weekStart": ""
}
~~~
