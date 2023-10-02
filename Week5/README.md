# ROS2 Tutorial: Intermediate
## Managing Dependencies with rosdep
### rosdep installation
If you are using rosdep within the ROS ecosystem, it is conveniently included with the ROS distribution, which is the recommended method for obtaining rosdep. You can install it by running:

```

apt-get install python3-rosdep
```
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/b8f55a7e-ba99-428b-a0a9-621fb5f30c20)

Note: For Debian and Ubuntu users, please ensure that you do not have a similarly named package called python3-rosdep2 installed before proceeding with the installation of python3-rosdep.

If you are using rosdep outside of ROS or the system package is unavailable, you can install it directly from PyPI using pip:

```bash

pip install rosdep
```

ROSdep Operation

Now that you have rosdep installed, you can use it to manage dependencies. If you are new to rosdep, make sure to initialize it with the following commands:

```bash

sudo rosdep init
rosdep update
```
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/642bc5c3-aaf8-415e-b57d-7f73c35e2250)

This initializes rosdep and updates the locally cached rosdistro index. Periodically updating rosdep is advisable to ensure you have the latest index.

To install dependencies, you can use rosdep install. Typically, you would run this command over a workspace containing multiple packages to install all dependencies. Here's an example command when in the root of the workspace with a 'src' directory that contains source code:

```bash

rosdep install --from-paths src -y --ignore-src
```
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/e4839ed9-ef0c-4e1c-94d8-ddad2bf9a333)

Breaking down the command:

    --from-paths src specifies the path to check for package.xml files to resolve keys.
    -y answers 'yes' to all prompts from the package manager, enabling unattended installation.
    --ignore-src instructs rosdep to ignore installing dependencies if the package itself is in the workspace.

Feel free to customize the rosdep install command as needed for your specific workspace and dependencies.
