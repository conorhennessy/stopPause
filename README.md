# About

stopPause is a project that turns a classic emergency stop button into a whackable pause button as a media key.
When the button is pressed a pause key is sent to the computer, conversely when the button is reset a pause key is sent.

![Photo of the emergency stop button with end of the cable hidden)](https://raw.githubusercontent.com/conorhennessy/stopPause/master/docs/StopPause_Photo1.jpg){:height="233px" :width="600px"}

__*Here it is in action...*__ [*And a video can be found here...*](https://photos.app.goo.gl/1bEmfZ5BV29aJBT9A)

![GIF of button being pressed with Spotify open, showing a song being paused](https://raw.githubusercontent.com/conorhennessy/stopPause/master/docs/StopPause.gif)


## How it's made  

Using an arduino ATmega32U4 the stop button is wired to digital PIN 2 with 5v supplied by the 5v PIN. With each loop of code, the arduino checks for a change of voltage to see if the button has been pressed or reset. The state change is then compared to the previous state to understand if to send a pause action.

(Wiring diagram coming here soon ;) )

![Photo of the inside of the emergency stop button with wiring and arduino visible](https://raw.githubusercontent.com/conorhennessy/stopPause/master/docs/StopPause_Photo2.jpg){:height="233px" :width="600px"}

## Create your own

If you fancy, you can create your own by following the above wiring diagram, getting the parts listed below and nicking my code on here if you fancy :)

## Built With

### Parts List  £££

* 1 Arduino Pro Micro ATmega32U4 - Bought [here](http://www.ebay.co.uk/itm/Pro-Micro-ATmega32U4-5V-16MHz-Replace-ATmega328-Arduino-Pro-Mini-PB/283126109094) on eBay = £4.43
* 1m Red 16AUG Gage Wire - Bought [here](https://www.ebay.co.uk/itm/Flexible-Silicone-Wire-Cable-8-10-12-14-16-18-20-22-24-28-30-AWG-Various-Colours/331718921763) on eBay = £1.70
* 1 Emergency Stop Button - Bought [here](https://www.ebay.co.uk/itm/Red-Sign-Mushroom-Emergency-Stop-Push-Button-Switch-Station-1-NC-Normally-C-KL-/223153590995) on eBay = £2.93
* 1 10kΩ Resistor - Donated to me by my housemate = Free
* Some Single Core blue Wire - Also donated from my housemate = Free
* Some Black Shrink Wrap - Nicked from my housemate, didn't make sense to go buying loads ;) = Free

__Overall cost of £9.06__

### Libraries

[HID](https://github.com/NicoHood/HID) - The HID Library used for the extra media control required for this project

## Contributors

* **Conor Hennessy** - *Creator* - [@conorhennessy](https://github.com/conorhennessy)
* **Alex Hockly** - *Contributor* - [@alhockly](https://github.com/alhockly)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details and that.

## Acknowledgments

* Acknowledgment to [@alhockly](https://github.com/alhockly) for his massive support in this project.  From getting me started to being my electronics consultant to debugging help. As this project was the first time I have dabbled with an arduino.
* [@orderedlist](https://github.com/orderedlist) for the minimal theme for GitHub Pages, found [here](https://github.com/pages-themes/minimal).
* [Instructables inspiration](https://www.instructables.com/id/USB-Volume-Control-and-Caps-Lock-LED-Simple-Cheap-/) - an instructibles guide for an arduino volume control, a guide that I found as some inspiration when creating this project
* This all started after me wanting to whack a button...
