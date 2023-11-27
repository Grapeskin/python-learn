#include "spdlog/spdlog.h"
#include <cstdio>
#include <iostream>

#include <nlohmann/json.hpp>

int main(int argc, char const *argv[]) {
  SPDLOG_INFO("Welcome to spdlog!");
  auto j3 = nlohmann::json::parse(R"({"happy": true, "pi": 3.141})");
  SPDLOG_INFO(j3.dump());
  nlohmann::json j;
  j["name"] = "zhangsan";
  j["age"] = 23;
  j["address"] = {"a", "b", "c"};
  j["address2"] = {{"k", "v"}, {"k1", "v1"}};
  SPDLOG_INFO(j.dump());
  return 0;
}
