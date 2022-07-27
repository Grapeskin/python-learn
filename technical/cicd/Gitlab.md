# Gitlab CICD

# Gitlab 安装

文档：`https://docs.gitlab.com/ee/install/docker.html`

```shell
sudo mkdir -p /opt/gitlab

export GITLAB_HOME=/opt/gitlab

sudo docker run --detach \
  --hostname 192.168.199.168:18080 \
  --publish 18443:443 --publish 18080:18080 --publish 18022:22 \
  --name gitlab \
  --restart always \
  --volume $GITLAB_HOME/config:/etc/gitlab \
  --volume $GITLAB_HOME/logs:/var/log/gitlab \
  --volume $GITLAB_HOME/data:/var/opt/gitlab \
  --shm-size 256m \
  gitlab/gitlab-ce:latest

sudo docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
```

# Gitlab Runner安装

文档：`https://docs.gitlab.com/runner/install/docker.html`

## docker runner

```shell
sudo mkdir -p /opt/gitlab-runner

sudo docker run -d --name gitlab-docker-runner-1 --restart always \
  -v /opt/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest

docker exec -it gitlab-docker-runner-1 bash

gitlab-runner register \
  --executor "docker" \
  --docker-image python:3.8-alpine \
  --url "http://192.168.199.168:18080/" \
  --registration-token "GR1348941VE6hHDvZ8JE99r_gaSQS" \
  --description "docker-runner" \
  --tag-list "docker" 
  
gitlab-runner verify
```

## shell runner

```shell
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash

sudo apt-get install gitlab-runner

sudo gitlab-runner register
  --executor "shell" \
  --url "http://192.168.199.168:18080/" \
  --registration-token "GR1348941VE6hHDvZ8JE99r_gaSQS" \
  --description "shell-runner" \
  --tag-list "shell"

sudo gitlab-runner verify

service gitlab-runner status 

sudo usermod -aG docker gitlab-runner

sudo systemctl restart docker
```