Notes on Windows-hosted Development Tools
=========================================

A number of development tools can be downloaded and installed on Windows.
As of this writing, the solutions are varied.
Please don’t consider this a how-to.
Rather, consider it a notebook of sorts.

**Installing GitHub Desktop (https://desktop.github.com/)**

Integration with VLab git seems to be about 80% there.
Configuration can be a hassle.
That said, I have found it to be pretty useful.

Download and install for this user only.
Installing for all users likely requires administrative privileges.

**Installing Git for Windows (https://git-scm.com/download/win)**

If GitHub Desktop did not install Git for Windows, download and install it now.

Use the Git Bash to perform the following installs whenever you can.
It’s so much easier than the MS DOS shell.

**Accessing VLab git from Windows via ssh**

It took a lot, but we’ve done it more than once now.  Here are some notes:

Create the folder .ssh in C:\Users\Firstname.Lastname.
I had to look up the DOS commands for this.
The Windows Explorer would not allow me to name a folder with a name that looked
like a file extension.
Git Bash did.
The .ssh folder needs to contain config and id_rsa.
I have id_rsa.pub in there too, but I doubt that it’s required.

.ssh/config contains the following.
Capitalization seems to matter here.

::

|  Host gerrit
|  Hostname vlab.ncep.noaa.gov
|     User firstname.lastname
|     Port 29418

::

.ssh/id_rsa contains the private key.
I was unable to use a key pair generated by puTTY.
Rather, I used ssh-keygen on MDLNet.
I followed the instructions on the VLab wiki for installing the public key on
VLab.
If you get all of this correct, you can do the following with Git Bash:

::

|  $ ssh -p 29418 Firstname.Lastname@vlab.ncep.noaa.gov
|
|    ****    Welcome to Gerrit Code Review    ****
|
|    Hi firstname.lastname, you have successfully connected over SSH.
|
|    Unfortunately, interactive shells are disabled.
|    To clone a hosted Git repository, use:
|
|    git clone ssh://firstname.lastname@vlab.ncep.noaa.gov:29418/REPOSITORY_NAME.git
|
|  Connection to vlab.ncep.noaa.gov closed.

::

**Configuring the Repository within GitHub Desktop**

On the Gerrit page for your project (e.g.,
https://vlab.ncep.noaa.gov/code-review/#/admin/projects/wisps),
Projects -> General, select Clone and ssh.
Find the command that looks like
“git clone ssh://matthew.peroutka@vlab.ncep.noaa.gov:29418/wisps”.
There’s a handy copy tool.
You won’t need the entire command, just the part that begins with “ssh://”.
On GitHub Desktop, File -> Clone repository.
Select URL tab.
Repository URL is the ssh string copied from Gerrit.
Local path is chosen by the user.

**Using GitHub Desktop**

Pulls and pushes to branches that are not controlled by Gerrit seem to work
pretty well.
Pushes to branches that are managed by Gerrit can be performed from
Repository -> Open in command prompt.
The command prompt supports a full range of git commands.

**Atom Text Editor**

Nice, context sensitive code editor with auto-completion and tons of plug-ins.
Very good integration with git and GitHub Desktop.
Download and install at https://atom.io/

Matt’s opinion:  Dark themes are very difficult to use.
Light themes are much easier.
For RST work, installed a package named language-restructuredtext.

**Install Python**

It seems that Python (https://www.python.org/downloads/) 3.6.15 will install
on our systems without privileges, but 2.7.15 will not.
WISPS development to date has used 2.7.
Sphinx seems to run fine under 3.6.15 and generates HTML.

**Install sphinx**

Those who are working on documentation may find sphinx useful.
Here’s the URL:  http://www.sphinx-doc.org/en/master/usage/installation.html

Launch Git for Windows -> Git Bash.
The command which pip will confirm that pip is installed and on the path.
The command pip install -U sphinx performs the installation of sphinx (and a
number of supporting packages).

**Install RTD (Read The Docs) theme for sphinx**

WISPS is using this theme within sphinx.
Others may do so in the future.
Here’s the URL:  https://github.com/rtfd/sphinx_rtd_theme

Again, within Git Bash, pip install sphinx_rtd_theme performs the installation.

**Windows shortcut to generate WISPS HTML documentation**

Again, this is a Windows-based technique that WISPS documentation authors
found useful.
The techniques used here may apply to other needs.
The steps are pretty much:

 * Switch to the build directory.
 * Set the environmental variable IGNORE_PDF to true.
 * Invoke make.bat.

All of this will fit into one Windows shortcut.
The syntax is ugly, but it works in both W7 and W10.
Here’s a URL that explains what’s going on:
https://stackoverflow.com/questions/3036325/can-i-set-an-environment-variable-for-an-application-using-a-shortcut-in-windows

Create a shortcut and name it appropriately.
The setup wizard is not very helpful for this task.
Right click the shortcut and edit its properties.
In the following steps, substitute the appropriate paths.
Set Target to C:\Windows\System32\cmd.exe /c "SET IGNORE_PDF=true && START /D ^"C:\Users\firstname.lastname\Documents\GitHub\wisps\docs^" make.bat html"
Set Start In to C:\Users\firstname.lastname\Documents\GitHub\wisps\docs

Here’s a different Target that does much the same:
C:\Windows\System32\cmd.exe /c "SET IGNORE_PDF=true && CD ^"C:\Users\Matthew.Peroutka\Desktop\VLabRepos\wisps\docs^" && START make.bat html
Once sphinx finishes building the HTML files, they will be stored on the PC
within the same docs tree.
In a web browser, access:
file:///C:/Users/firstname.lastname/Documents/GitHub/wisps/docs/build/html/index.html

*Original by Matt Peroutka, May 2018*
