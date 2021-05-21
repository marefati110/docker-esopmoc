<h3 align="center">mysql-pydump</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub license](https://img.shields.io/github/license/marefati110/mysql-pydump)](https://github.com/marefati110/mysql-pydump/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/marefati110/mysql-pydump)](https://github.com/marefati110/mysql-pydump/issues)
[![GitHub forks](https://img.shields.io/github/forks/marefati110/mysql-pydump)](https://github.com/marefati110/mysql-pydump/network)
[![GitHub stars](https://img.shields.io/github/stars/marefati110/mysql-pydump)](https://github.com/marefati110/mysql-pydump/stargazers)
[![Documentation Status](https://readthedocs.org/projects/mysql-pydump/badge/?version=latest)](https://mysql-pydump.readthedocs.io/en/latest/?badge=latest)

</div>

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

### Installing

```bash
git clone https://github.com/marefati110/docker-composer.git
cd docker-esopmoc
pip3 install -r ./requirement.txt
```

## 🎈 Usage <a name="usage"></a>

### general usage

```bash
python3 ./docker-esopmoc.py options args
```

#### generate by container name

```bash
python3 ./docker-esopmoc.py -c mongo mysql
```

#### generate by container id

```bash
python3 ./docker-esopmoc.py -c 94409bee9f87 9c70eed2f9c6
```

#### generate by network name

```bash
python3 ./docker-esopmoc.py -n nginx
```

## ✍️ Authors <a name = "authors"></a>

- [@marefati](https://github.com/marefati110) - Idea & Initial work
- marefati110@gmail.com
