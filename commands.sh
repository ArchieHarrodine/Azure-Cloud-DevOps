ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub
git clone git@github.com:<organisation_name>/<repository_name>.git

python -m venv .venv
source .venv/bin/activate
cd <repository_name>
pip install -r requirements.txt

az webapp up \
  --name <app_name> \
  --resource-group <resource_group> \
  --sku B1 \
  --logs \
  --runtime "PYTHON:3.10"

chmod +x make_predict_azure_app.sh
./make_predict_azure_app.sh

ssh <username>@<pub_ip_address>

sudo snap install docker
sudo groupadd docker
sudo usermod -aG docker $USER

curl -O <download_link>
mkdir myagent && cd myagent
tar zxvf ../<vsts-agent-linux>
./config.sh

sudo ./svc.sh install
sudo ./svc.sh start

sudo apt-get update
sudo apt install -y software-properties-common python3.10 python3.10-venv python3-pip python3.10-distutils zip pipx
export PATH=$HOME/.local/bin:$PATH
pipx install pylint

./make_predict_azure_app.sh