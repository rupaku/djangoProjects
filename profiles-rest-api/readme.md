#### Installation Guide
##### install GIT
#### install virtual box for windows host
#### install vagrant for windows 64 bit
#### install atom
#### install modheader to chrome extension

### create vagrant file
#### vagrant init ubuntu/bionic64

#### to run vagrant file
#### vagrant up

#### connect to machine
#### vagrant ssh

#### to logout
#### exit

#### inside virtual machine vagrant server
#### cd /vagrant

#### python -m venv ~/env
#### source ~/env/activate

#### pip install -r requirements.txt

#### django-admin startproject profiles_project .

#### python manage.py startapp profiles_api

#### python manage.py runserver 0.0.0.0:8000

#### python manage.py makemigrations profiles_api

#### python manage.py migrate

#### python manage.py createsuperuser
#### email:rupakumari201@yahoo.com ,user:rupa,password:rupa

#### GET request :http://127.0.0.1:8000/api/hello-view/

#### user profile :http://127.0.0.1:8000/api/profile/

#### login :http://127.0.0.1:8000/api/login/ token is generated on post

#### user feed :http://127.0.0.1:8000/api/feed/

### Deploy code to AWS server
#### cat ~/.ssh/id_rsa.pub
#### add this key pair in amazon key pair section under services->ec2->network->key-pair
#### create ec2 instance-> launch instance
#### choose amazon machine image as "ami-07dc734dc14746eab" for ubuntu
#### select micro instance
#### configure instance
#### configure security group -> SSH  and HTTP
#### ssh ubuntu@<dns server>
#### run below command on server
#### curl -sL https://raw.githubusercontent.com/rupaku/djangoProjects/master/profiles-rest-api/deploy/setup.sh | sudo bash -
#### change in allowed hosts and push and run update.sh on dns server 

