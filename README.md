# Tournament Results

## Installation
Install [Vagrant](http://vagrantup.com/)<br>
Install [VirtualBox](https://www.virtualbox.org/)<br>
Clone [this project](https://github.com/frost-byte/fullstack-nanodegree-vm.git)<br>

1. **Use One of the Following Programs**
    - Git Bash on Windows
    - Terminal on Mac
    - Shell on Linux
&nbsp;
- **Navigate to the vagrant folder in the cloned repository.**
- Type the command **vagrant up**
- Type **vagrant ssh** to connect to the vagrant VM. (see below for setting up SSH on Windows)

Check the section **Using the Vagrant Virtual Machine** [here](https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true) for more information.<br>

## SSH on Windows
If you opt to use cmd.exe in Windows, you will be able to bring up the Vagrant VM.
However, when you try to use "vagrant ssh" you will probably receive a message similar to the following:
```
`ssh` executable not found in any directories in the %PATH% variable. Is an
SSH client installed? Try installing Cygwin, MinGW or Git, all of which
contain an SSH client. Or use your favorite SSH client with the following
authentication information shown below:

Host: 127.0.0.1
Port: 2222
Username: vagrant
Private key: C:/Path/to/fullstack-nanodegree-vm/vagrant/.vagrant/machines/default/virtualbox/private_key
```
In the repository's subdirectory, **vagrant/.vagrant/machines/default/virtualbox**,
there is a file called *private_key*

On Windows you can use the [PuTTY Key Generator - PuTTYgen](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) to convert the contents of that file into the *.ppk file you will use in PuTTY to ssh into the Vagrant/VirtualBox VM.

To convert the provided private_key file you will need to select "Import Key" under "Conversions"in PuTTY Key Generator.
Specify the location of the "private_key" file and then click the "Save private key" button.
When asked about saving the key without a passphrase, select yes. This will generate a private key file with the .ppk extension.

Once the file is saved you can then follow use the guide under the [References SSH](#SSH) section.
Use the following configuration in PuTTY:<br>

###Session
**Host Name**:  ```127.0.0.1``` or ```localhost```

###Connection -> Data
**Auto-login username**: ```vagrant```

###Connection -> SSH -> Auth
**Private key file for authentication**: Browse to the .ppk file you created using PuTTY Key Generator.

Once you've specified the above, go back to "Session" and under "Saved Sessions" enter a name for your config and click the "Save" button to the right of the list of Saved Sessions.

From this point on all you'll have to do to start the session is open PuTTY and double click on your config in the Saved Sessions list.


## Running the Unit Tests

1. Connect to Vagrant using SSH
- cd vagrant
- psql
- \i tournament.sql
- \q
- python tournament_test.py

## Requirements
+ Vagrant VM
+ VirtualBox
+ Clone of this Repository

## Recommended
+ Sphinx
+ flake8

```
sudo pip install Sphinx
sudo pip install flake8
```
##References
###Code Documentation
[Documentation](https://frost-byte.github.io/fullstack-nanodegree-vm/) for the modules was generated using Docstrings and Sphinx.<br>

###Code Formatting
[Pep8 Online](http://pep8online.com/)<br>
An online python formatting tester.

[Flake8](https://flake8.readthedocs.org/en/2.4.1/)<br>
A Handy, command line tool for checking the formatting of your python code.

###Code Attributions
Most of my code was written using PostGreSQL Functions and Types that are in the tournament.sql file.
The queries and functions I created were combinations of techniques found in the links under the PostGreSQL section below.
###Other API and Coding References
[Stack Overflow](http://stackoverflow.com/)<br>
A go to resource for solving all problems related to coding.

[W3Schools](http://www.w3schools.com/)<br>
Great reference for all languages and specifications for programming web based content. HTML, CSS, jQuery, Javascript...

###PostGreSQL
[PostGreSQL Docs](http://www.postgresql.org/docs/)<br>
[Return Multiple Fields in PostGreSQL](http://stackoverflow.com/questions/4547672/return-multiple-fields-as-a-record-in-postgresql-with-pl-pgsql)<br>
[Return Setof Records](http://stackoverflow.com/questions/955167/return-setof-record-virtual-table-from-function)<br>
[Store a Query Result in a Variable](http://stackoverflow.com/questions/12328198/store-the-query-result-in-variable-using-postgresql-stored-procedure)<br>
[Store Table Results from Two Queries, Columns](http://stackoverflow.com/questions/12921226/how-to-join-result-of-two-sql-statements-into-one-table-and-different-columns)<br>
[PostGreSQL CREATE FUNCTION return Types](http://www.postgresqlforbeginners.com/2010/12/create-function-return-types.html)<br>
[Quick Guide to writing PLPGSQL Functions](http://www.postgresonline.com/journal/archives/76-Quick-Guide-to-writing-PLPGSQL-Functions-Part-2.html)<br>
[psql Commands and Options](http://momjian.us/main/writings/pgsql/aw_pgsql_book/node142.html)<br>
###SSH
[How To Use SSH Keys with PuTTY and PuTTYGen](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-keys-with-putty-on-digitalocean-droplets-windows-users)<br>
[PuTTY for Windows](http://www.chiark.greenend.org.uk/~sgtatham/putty/)<br>

###Markdown

[Online Markdown Editor](http://markable.in/editor/)<br>
Incredibly useful for troubleshooting and learning markdown.