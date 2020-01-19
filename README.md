# Kinect VLC Interface

Application to pause and play a video playing on VLC through the VLC web interface using gestures on kinect for XBOX One.

This is part of the first lab of Human Computer Interface Course.

## Software Architecture 
We use the Vitruvius utilities to read the gestures from the Kinect to our WPF Application. We used the sample Gesture Control Application from their repository as a base for our application.
[LightBuzz-Vitruvius Repository](https://github.com/LightBuzz/Vitruvius)

We used the SwipeLeft Gesture for pause and SwipeRight Gesture for play.

This WPF application then ran a python script whenever a recognized gesture was invoked

We used a python script to control the VLC player through the VLC web interface. The python script sent the appropriate GET requests to the VLC web interface to generate the appropriate output.
[VLC Web Interface Documentation](https://wiki.videolan.org/Documentation:Modules/http_intf/)


[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbkFbS2luZWN0XSAtLSBWaXRydXZpdXMgLS0-IEJbV1BGIEFwcGxpY2F0aW9uXVxuQltXUEYgQXBwbGljYXRpb25dLS0gU2VuZHMgUmVjb2duaXplZCBHZXN0dXJlcyAtLT4gQ1tQeXRob24gU2NyaXB0XVxuQ1tQeXRob24gU2NyaXB0XS0tIFNlbmRzIEdFVCBSZXF1ZXN0cyAtLT4gRFtWTEMgV2ViIEludGVyZmFjZV1cbkRbVkxDIFdlYiBJbnRlcmZhY2VdLS0-IEVbVkxDIEFwcGxpY2F0aW9uXSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In19)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbkFbS2luZWN0XSAtLSBWaXRydXZpdXMgLS0-IEJbV1BGIEFwcGxpY2F0aW9uXVxuQltXUEYgQXBwbGljYXRpb25dLS0gU2VuZHMgUmVjb2duaXplZCBHZXN0dXJlcyAtLT4gQ1tQeXRob24gU2NyaXB0XVxuQ1tQeXRob24gU2NyaXB0XS0tIFNlbmRzIEdFVCBSZXF1ZXN0cyAtLT4gRFtWTEMgV2ViIEludGVyZmFjZV1cbkRbVkxDIFdlYiBJbnRlcmZhY2VdLS0-IEVbVkxDIEFwcGxpY2F0aW9uXSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In19)

## How to Use

### VLC Web Interface
Enable control through VLC web interface by following the instruction in the [documentation](https://wiki.videolan.org/Documentation:Modules/http_intf/#VLC_2.0.0_and_later)

### WPF Application


Change the path to the python file depending on your path in [GesturesPage.xaml.cs file](WPF/Program_files/GesturesPage.xaml.cs).

```cs
start.FileName = "C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python37\\python.exe";
```

You will have to change the password to the one you have set for your web interface. Change the following line in the [GesturesPage.xaml.cs file](WPF/Program_files/GesturesPage.xaml.cs).
```cs
start.Arguments = string.Format("{0} {1} {2}", "C:\\Users\\admin\\Desktop\\script.py", tblGestures.Text,"{password}");
```


Open the [VLC_Control.sln](WPF/Program_files/VLC_Control.sln) file in Visual Studio on Windows 10. Run the project.



### Gestures

* *SwipeLeft* to pause a video
* *SwipeRight* to play a video 

## Futher Work
- [ ]  Add an input box on the application to that the user may enter his password associated with the web interface
- [ ]  Create the GET requests from the WPF application directly instead of through the python script
- [ ] Add more gestures and maybe also custom gestures to control other aspects of the web player.

To edit this repo following lines are important

Runs the python script with the Gesture name as argument

[GesturesPage.xaml.cs file](WPF/Program_files/GesturesPage.xaml.cs)
```
start.Arguments = string.Format("{0} {1} {2}", "C:\\Users\\admin\\Desktop\\script.py", tblGestures.Text,"1234");
```

[script.py](WPF/Program_files/script.py) performs actions based on what arguments are provided. It makes GET requests to the web interface for VLC player based on the documentation.



## Contributors

[Rhevanth M (17IT133)](https://github.com/Rhevanth)

[Pranav P (17IT229)](https://github.com/pran-p)

[Ryan Rozario(17IT134)](https://github.com/ryan-rozario)


#### Demo Video
[![Watch the video](https://i.ytimg.com/vi/AjWfY7SnMBI/maxresdefault.jpg)](https://videobin.org/+15ou/1bog.ogg)