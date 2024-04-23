# PAIS Accomplishments

## About
A small tool for generating and transformation accomplishments from BibTex format files.

## Homepage
PYPI: https://pypi.org/project/pais-accomplishments-tool/

## Quick start

### Install

For install package run it.
```shell
pip install pais-accomplishments-tool
```

### Upgrade
For upgrade tools to latest version run it
```shell
pip install pais-accomplishments-tool --upgrade
```

### Dependencies



### Add to PATH

#### On Mac + zsh
```shell
nano ~/.zshrc
```
And the following line to the `.zshrc` with the actual path of the [package_name] script
```shell
export PATH="/path/to/package:$PATH"
```
For Python 3.15 on MacOS 14
```shell
export PATH="/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pais-accomplishments-tool/paisAccTool.py:$PATH"
```

#### On Mac and Linux + bash
```shell
nano ~/.bash_profile
```
And the following line to the `.bash_profile` with the actual path of the [package_name] script
```shell
export PATH="/path/to/package:$PATH"
```
For Python 3.15 on MacOS 14
```shell
export PATH="/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pais-accomplishments-tool/paisAccTool.py:$PATH"
```

### Simple use
#### Help
For watch help message run [paisAccTool.py](pais-accomplishments-tool/paisAccTool.py):
```shell
python3 paisAccTool.py -h
```

#### Sample
For watch to work run [paisAccTool.py](pais-accomplishments-tool/paisAccTool.py) for [sample accomplishments file](accomplishments_sample.bib) it
```shell
python3 paisAccTool.py accomplishments_sample.bib -c -en
```
Terminal output: 
```shell
Hello everyone!
This is the micro tools for contain and formating accomplishments from BibTex source
 [ ]  misc accomplishment: rand1        done
 [ ]  misc accomplishment: rand2        done
 [ ]  misc accomplishment: rand3        done
 [ ]  misc accomplishment: rand4        done
1. Наставник образовательной программы Звездный путь.Зима, Иван Иванов, Московского государственного университета, 2.2023
2. Наставник образовательной программы Тёмная материя.Весна, Мария Петрова, Санкт-петербургского государственного университета, 4.2023
3. Победитель образовательной программы Космос.Лето, Алексей Сидоров, Новосибирского государственного университета, 6.2023
4. Участник олимпиады искусственный интеллект.Осень, Екатерина Кузнецова, Томского государственного университета, 9.2023

```
#### Common usage format
```shell
python3 paisAccTool.py <source .bib file> [-d <destination>, -t "template string", -m "field" "for" "transformation", -c, -en]
```

-
- `-t "template"` contain a python string template that will be used to generate the list of accomplishments. **Important, a template can only contain the bibtex field names of an object**;
- `-m <"words", " " ..>` contain bibtex fields of the object, which are required to be put in the gent case;
- `-c` mean that each new entry will start with a capital letter;
- `-en` mean that the list of accomplishments will be output with numbering.

```shell
The micro tools for contain and formating accomplishments from BibTex source

positional arguments:
  source                Path to source .bib file

options:
  -h, --help            show this help message and exit
  -d DESTINATION, --destination DESTINATION
                        Path to destination .bib file
  -t TEMPLATE, --template TEMPLATE
                        A template string for generating accomplishment string. Default: {prefix} {type} {title}, {author}, {organization}, {month}.{year}
  -m MORPHS [MORPHS ...], --morphs MORPHS [MORPHS ...]
                        A list of fields for morphological transformations. Default: ('type', 'organization')
  -c, --capitalize      Flag
  -en, --enumerate      Flag

```

#### Other usage sample
Command to output the list of accomplishments to a file
```shell
python3 paisAccTool.py accomplishments_sample.bib -c -en -d output.txt
```

Command with its own output template
```shell
python3 paisAccTool.py accomplishments_sample.bib -t "{prefix} {type} {title}, {author}, {organization}, {location} {start}-{end}"
```

Command with its own morphological transformations fields
```shell
python3 paisAccTool.py accomplishments_sample.bib -m "title", "author", "type"
```

### Accomplishments format

Each accomplishment is stored in a .bib file in bibtex format.
Below are the fields that are used to store achievements:
```bibtex
@misc{identifier,
	prefix = {Твоя роль на мероприятии},
	title = {Название мероприятия},
	type = {Тип мероприятия},
	author = {ФИО},
	organization = {Организация, которая проводит мероприятие},
	section = {Секция на конференции или номинация на олимпиаде, и тп.},
	location = {Место проведения},
	url = {url подтверждения достижения},
	start = {дата начала},
	end = {дата окончания},
	year = {год},
	month = {месяц},
	certificate = {результат, документ подтверждающий результат или участие (диплом, ...)},
	order = {место в конкурсе или статус на мероприятии}
}
```
If you do not have a field to enter your specific information, you can add such a field:
```bibtex
    <key> = {value}
```
The Accomplishments.bib file can be stored locally on your pc or in a remote git repository, so every commit means a new achievement (very convenient).

