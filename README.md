# Projeto: BK-cells
## version: v1.1.0 InProgress

## Contribuintes:
  - Pesquisador:
    - Dr. Ramón Enrique Ramayo González
      - CV Lattes: [Gonzales, R.E.R.](http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4266447Z9)
  - Desenvolvedor:
    - Iury Adones Xavier dos Santos
      - CV Lattes: [Xavier-Santos, I.A.](http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4805442U6)
      - Github: [iuryxavier](https://github.com/iuryxavier)


## Estrutura do Projeto em árvore
### BK_cells

```bash
$ tree
.
├── projeto_null
│   ├── agatha_null.py
│   └── README_null.md
├── projeto_one
│   ├── agatha_one.py
│   └── README_one.md
├── projeto_three
│   ├── agatha_three.py
│   └── README_three.md
├── projeto_two
│   ├── agatha_two.py
│   └── README_two.md
├── README.md
└── requirements.txt

4 directories, 10 files
```

# Intall Python
## Versão Python 2.7.13 | Version Python 2.7.13
## Ubuntu & LinuxMint
### Instalar Pacotes Requeridos | Install Required Packages

```bash
$ sudo apt-get install build-essential checkinstall -y
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev -y
```

### Baixar Python 2.7.13 | Download Python 2.7.13

```bash
$ cd /usr/src
$ wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
$ tar xzf Python-2.7.13.tgz
```

### Compilar o Python | Compile Python Source

```bash
$ cd Python-2.7.13
$ sudo ./configure
$ sudo make altinstall
```

### Conferir a Versão Python | Check the Python Version

```bash
$ python2.7 -V
Python 2.7.13
```

### Referência | Reference:
#### [How to Install Python 2.7.13 on Ubuntu & LinuxMint](http://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/)

## Arch Linux

```bash
$ sudo pacman -S python2
$ python2 -V
Python 2.7.13
```

---------------------------------------------------------------

#  virtualenv: Virtual Python Environment builder
Ambiente Isolado para Python com virtualenv, não afeta o python instalado de forma global

## Instalar o vitualenv no Ubuntu & LinuxMint | Install virtualenv in Ubuntu & LinuxMint

```bash
$ sudo apt-get install python-pip
```

### Preparando o Projeto BK_cells v1.1.0

```bash
$ cd ~
$ mkdir project_bk_cells
$ cd project_bk_cells
$ which python2.7
/usr/bin/python2.7  
$ virtualenv -p /usr/bin/python2.7 venv
$ ls
venv
$ source venv/bin/activate
(venv) $ python -V
Python 2.7.13
(venv) $ mkdir BK_cells
(venv) $ ls
venv BK_cells
(venv) $ git clone -b 'v1.1.0' https://github.com/rramayo/BK-cells BK_cells
Obs: git clone -b <name_of_the_tag> <repository_url> <destination>
(venv) $ cd BK_cells
(venv) $ ls
projeto_null  projeto_three  README.md
projeto_one   projeto_two    requirements.txt
(venv) $ pip install -r requirements.txt
```

### Executar o Programa projeto_null/agatha_null.py

```bash
(venv) $ ls
projeto_null  projeto_three  README.md
projeto_one   projeto_two    requirements.txt
(venv) $ cd projeto_null
(venv) $ python agatha_null.py
```

### Executar o Programa projeto_one/agatha_one.py

```bash
(venv) $ ls
projeto_null  projeto_three  README.md
projeto_one   projeto_two    requirements.txt
(venv) $ cd projeto_one
(venv) $ python agatha_one.py
```

### Executar o Programa projeto_two/agatha_two.py

```bash
(venv) $ ls
projeto_null  projeto_three  README.md
projeto_one   projeto_two    requirements.txt
(venv) $ cd projeto_two
(venv) $ python agatha_two.py
```

### Executar o Programa  projeto_three/agatha_three.py

```bash
(venv) $ ls
projeto_null  projeto_three  README.md
projeto_one   projeto_two    requirements.txt
(venv) $ cd projeto_three
(venv) $ python agatha_three.py
```

### Comando para desativar o virtualenv | Command to Disable virtualenv

```bash
(venv) $ deactivate
$
```

## Instalar o vitualenv no Arch Linux | Install virtualenv in Arch Linux

```bash
$ sudo pacman -S python2-virtualenv
```

### Preparando o Projeto BK_cells v1.1.0

```bash
$ cd ~
$ mkdir project_bk_cells
$ cd project_bk_cells
$ which python2
/usr/bin/python2
$ virtualenv -p /usr/bin/python2 venv
$ ls
venv
$ source venv/bin/activate
(venv) $ python -V
Python 2.7.13
(venv) $ mkdir BK_cells
(venv) $ ls
venv BK_cells
(venv) $ git clone -b 'v1.1.0' https://github.com/rramayo/BK-cells BK_cells
Obs: git clone -b <name_of_the_tag> <repository_url> <destination>
(venv) $ cd BK_cells
(venv) $ ls
projeto_null  projeto_three  README.md
projeto_one   projeto_two    requirements.txt
(venv) $ pip install -r requirements.txt
```

### Executar o Programa projeto_null/agatha_null.py

```bash
(venv) $ ls
projeto_null  projeto_three  README.md
projeto_one   projeto_two    requirements.txt
(venv) $ cd projeto_null
(venv) $ python agatha_null.py
```

### Executar o Programa projeto_one/agatha_one.py

```bash
(venv) $ ls
projeto_null  projeto_three  README.md
projeto_one   projeto_two    requirements.txt
(venv) $ cd projeto_one
(venv) $ python agatha_one.py
```

### Executar o Programa projeto_two/agatha_two.py

```bash
(venv) $ ls
projeto_null  projeto_three  README.md
projeto_one   projeto_two    requirements.txt
(venv) $ cd projeto_two
(venv) $ python agatha_two.py
```

### Executar o Programa  projeto_three/agatha_three.py

```bash
(venv) $ ls
projeto_null  projeto_three  README.md
projeto_one   projeto_two    requirements.txt
(venv) $ cd projeto_three
(venv) $ python agatha_three.py
```

### Comando para desativar o virtualenv | Command to Disable virtualenv

```bash
(venv) $ deactivate
$
```
