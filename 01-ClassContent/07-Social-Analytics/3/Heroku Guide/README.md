## Heroku Deployment Guide

* Heroku is a cloud application platform. This means that we can run our scripts on Heroku's servers! Here are the steps to do get our apps running on Heroku.

* Important: before deploying your code to a cloud server, verify that it runs without error locally (i.e. be able to run it from your console or in Jupyter Notebook without errors).

* Push your code to Github. Include both the `Procfile` and `requirements.txt` files in the directory. 

* Open your `Procfile` with a text editor, and replace `ChatterBot.py` with the name of your Python script.

  ![procfile](Images/procfile.png)

* Your `requirements.txt` should list the required modules, and their versions. Here, we require only the `tweepy` module, version `3.5.0`. You can run `conda list` from your console to display all the modules you have installed, as well as their version numbers.

  ![requirements](Images/requirements.png)

* Next, go to [heroku.com](heroku.com) and create an account.

* After registering, click on `New`, then on `Create new app`. You will create a new `app` for each program.

  ![heroku1.png](Images/heroku1.png)

* In the next screen, create your `App name`, a unique and meaningful name for your app. Click on `Create app`. 

  ![heroku2.png](Images/heroku2.png)

* Next, select `Connect to Github`, and click the button at the bottom.

  ![heroku3.png](Images/heroku3.png)

* In the field `repo-name`, enter the name of your Github repo, and click `Search`.

  ![heroku4.png](Images/heroku4.png)

* Click `Connect` to link your Heroku app with your Github repo.

  ![heroku5.png](Images/heroku5.png)  

* Click on `Enable Automatic Deploys`, which will allow the Heroku server to restart your app whenever you push a change to your Github repo.

  ![heroku6.png](Images/heroku6.png)  

* Finally, click on the `Resources` tab, followed by clicking the `edit` button with the pencil icon.

  ![heroku7.png](Images/heroku7.png)

* Slide the worker switch to the right, then click on `Confirm`.

  ![heroku8.png](Images/heroku8.png)  

* Your app should now be deployed!  
