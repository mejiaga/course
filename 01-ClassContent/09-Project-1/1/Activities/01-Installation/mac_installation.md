# Mac MySQL Installation

You will require admin privileges to install MySQL on your Mac. 

## MySQL Server

* Download **MySQL Community Server 5.7** from [MySQL Server](https://dev.mysql.com/downloads/mysql/5.7.html#downloads) choosing the DMG option.

* Follow the installation [instructions](https://dev.mysql.com/doc/refman/5.7/en/osx-installation-pkg.html).

* During setup a temporary password will be given. Be sure to write this down!  You will need it shortly.

![temp root password](../Images/mac-installer-root-password.png)

* Once the download has been completed, the MySQL application should have been installed inside your `/usr/local` directory.  There will be a symlink that points to the currently installed version.  From a terminal window, type `ls -Gal /usr/local` and check that the output includes something like the following lines:

```
lrwxr-xr-x    1 root              wheel    30 Jul  9 09:06 mysql -> mysql-5.7.22-macos10.13-x86_64
drwxr-xr-x   13 root              wheel   416 Jul  9 09:06 mysql-5.7.22-macos10.13-x86_64
``` 

* Open up your Mac's System Preferences.  Find the newly-created MySQL panel.  If the MySQL server isn't already running, you should click the button labeled "Start MySQL Server".  This will require administrator privileges.

* Edit your `$PATH` variable to include the `/usr/local/mysql/bin` path.  Add a line like the following to your `~/.bash_profile`:

```
export PATH="/usr/local/mysql/bin:$PATH"
```

Then source the file: `source ~/.bash_profile` 

Test that the executable is now locatable:

```
which mysql
```

Should return `/usr/local/mysql/bin/mysql`

* From the terminal, run `mysql -u root -p`. With the following prompt, enter the temporary password that you recorded previously. If everything works, your terminal will now be in the MySQL Command Line Interface (also referred to as CLI).

* The next step is to change the temp password to a personal password. From the mysql CLI run the command `ALTER USER 'root'@'localhost' IDENTIFIED BY '<your new password>';` Where `<your new password>` is your newly created password.

* Finally, check the new password by exiting mysql CLI  with `exit`, then start the MySQL CLI again with `mysql -u root -p`. Log in with the newly created password to confirm the change.

* Remember the new password you created for future use.


### Troubleshooting

If you get an error like the following:

```
-bash: mysql: command not found
```

It could mean that the `mysql` executable is not in your `$PATH`.  

Did you make sure that the MySQL server is running?  Check the MySQL panel in System Preferences or examine the running system processes using `ps`: 

```
ps aux | grep mysqld
```

This should show that the `/usr/local/mysql/bin/mysqld` executable is running.


## MySQL Workbench

* Download [MySQL Workbench](https://www.mysql.com/products/workbench/).

* Once the download has finished, open the installer and run through the installation. This process should be more straightforward opposed to the server.

* Open up MySQL Workbench after installation.
