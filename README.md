# Projeto: BK-cells
## version: v1.0.0

## Contribuintes:

  - Pesquisador:
    - Dr. Ramón Enrique Ramayo González
      - CV Lattes: [Gonzales, R.E.R.](http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4266447Z9)
  - Desenvolvedor:
    - Iury Adones Xavier dos Santos
      - CV Lattes: [Xavier-Santos, I.A.](http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4805442U6)
      - Github: [iuryxavier](https://github.com/iuryxavier)

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
$ sudo python2.7 -m pip install -U pip
$ sudo python2.7 -m pip install -U virtualenv
```

## Instalar o vitualenv no Arch Linux | Install virtualenv in Arch Linux

```bash
$ sudo pacman -S python2-virtualenv
```

### Preparando o Projeto BK_cells v1.0.0 |

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
(venv) $ cd BK_cells
(venv) $ git init
(venv) $ git remote add origin
```

### Comando para desativar o virtualenv | Command to Disable virtualenv

```bash
(venv) $ deactivate
$
```
