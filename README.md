<h3 align="center">docker-esopmoc</h3>

![compose (1)](https://user-images.githubusercontent.com/42033084/119117077-1f40a100-ba3e-11eb-9d2b-8b33b51c4a4e.jpg)

---

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

docker-esopmoc generate docker-compose file from running container just vice versa of docker-compose

## 🏁 Getting Started <a name = "getting_started"></a>

### reuirements

```
python > 3.5
pip = 3
```

### Installing

#### auto install

```bash 
curl https://raw.githubusercontent.com/marefati110/docker-esopmoc/main/install.sh | sh
```

#### manual install

```bash
git clone https://github.com/marefati110/docker-esopmoc.git
cd docker-esopmoc
pip3 install -r ./requirement.txt
```

## 🎈 Usage <a name="usage"></a>

### help

```bash
python3 ./docker-esopmoc.py -h
```

### general usage

```bash
python3 ./docker-esopmoc.py options args
```

#### generate docker-compose.yaml by container name

```bash
python3 ./docker-esopmoc.py -c mongo mysql
```

#### generate docker-compose.yaml by container id

```bash
python3 ./docker-esopmoc.py -c 94409bee9f87 9c70eed2f9c6
```

#### generate docker-compose.yaml by network name

```bash
python3 ./docker-esopmoc.py -n nginx
```

## ✍️ Authors <a name = "authors"></a>

- [@marefati](https://github.com/marefati110) - Idea & Initial work
- marefati110@gmail.com
