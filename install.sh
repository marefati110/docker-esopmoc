mkdir -p ~/.docker-esopmoc
cd ~ 
git clone https://github.com/marefati110/docker-esopmoc.git
cd docker-esopmoc
pip3 install -r ./requirement.txt
echo "alias docker-esopmoc='python ~/docker-esopmoc/docker-esopmoc.py'" >> ~/.bashrc
