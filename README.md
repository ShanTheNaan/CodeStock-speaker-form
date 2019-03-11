# CodeStock-speaker-feedback 

This project was created to fullfill the need for a digitized and
semi-automated feedback system for CodeStock speakers. Both the speakers
themselves as well as organizers need to have access to as much feedback from
the conference attendees as possible in order to improve and continue to
provide the best experience possible. In order to maximize the feedback
participation from the attendees, the feedback system is simplistic and easy to
access by using QR codes. 

## Getting Started

These instructions detail how to use the system from both the admin and the end
user perspectives.

### Prerequisites -- Admins

Admins will need a hosting environment capable of serving the anticipated
traffic to the site during the conference. They will also, in addition to the
python package requirements, will need a MySQL database. The necessary steps to 
install MySQL dependencies are shown in the Installing section

### Prerequisites -- End Users

End users will simply need a smartphone with a camera and the desire to give
useful feedback so that their conference can be improved year-over-year. 

### Installing

On Ubuntu, install the following before installing the Python3 dependencies:
```
sudo apt install python3-dev
```
```
sudo apt install libmysqlclient-dev 
```
```
sudo apt install gcc
```

Then install python dependencies as normal with:
```
pip install -r requirements.txt
```

### Initialize Database

Lorem ipsum

### Editing With the Admin Console

Lorem ipsum

### Deployment

Lorem ipsum

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the [tags on this repository](https://github.com/ShanTheNaan/CodeStock-speaker-feedback/tags). 

## Authors

* **Colin Mawhinney** - [Colsarcol](https://github.com/Colsarcol)
* **Michael Xie** - [px1624](https://github.com/px1624)
* **Shan Lalani** - [ShanTheNaan](https://github.com/ShanTheNaan)
* **Zachary Trzil** - [ztrzil](https://github.com/ztrzil)

## License

This project is licensed under the 3-Clause BSD License - see the
[LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* We'd like to thank those that made KnxHx possible, as that allowed us the
opportunity to create a solution to this need by the CodeStock organizers.
