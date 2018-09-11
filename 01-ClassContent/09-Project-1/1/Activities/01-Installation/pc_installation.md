# Windows MySQL Installation

* Download the MySQL installer from [here](https://dev.mysql.com/downloads/windows/installer/5.7.html) and be sure to choose the larger of the two options.

  ![Mysql download](../Images/pc_mysql_download.png)

* After the download has finished, open and run the installer.

* Agree to license then select **Developer Default** as the type of setup and click next.

  ![developer default](../Images/mysql_install_option.png)

* Continue clicking moving on to finish the installation. Once complete, click `execute` in the installation section. This will take a some time while it downloads and installs the necessary programs.

  ![mysql_install_option](../Images/mysql_installing.png)

* If you come across the error `One or more product requirements have not been satisfied`, click yes to continue.

* Once everything has been installed you will be directed the next part of the setup. Keep the default options as you continue through the next two steps.

  ![mysql install part 2](../Images/mysql_standalone.png)

* Next, you will be at the **Accounts and Roles** page. Create and record a root password for MySQL that you will remember. This will be used to connect your MySQL server locally and will cause issues if you forget.

  ![root password](../Images/mysql_root_pw.png)

* Continue through the rest of the set up keeping everything default. Once everything has finished, the MySQL Shell and MySQL Workbench will open. Exit the shell and keep the workbench open.
