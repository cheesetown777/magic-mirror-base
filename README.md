# Magic Mirror (ReadMe is still WIP)

[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)]()
[![Python2](https://img.shields.io/badge/python-2.7-blue.svg)]()
[![licence](https://img.shields.io/badge/licence-GPLv3-blue.svg)]()
[![OpenSource](https://badges.frapsoft.com/os/v2/open-source.svg?v=102)]()

Open Source Smart Mirror software for Raspberry PI. Keep in my software is still under construction, thus a little buggy :wink:

## Installation

Open up terminal on raspberry pi and type this in.

```bash
curl -sL https://raw.githubusercontent.com/Techblogogy/magic-mirror-base/master/installer/install.sh | bash
```

This will automatically download magic mirror software and install it. Before use you'll have to edit this `~/.local/share/mirror_server/config.cfg` with correct API keys, audio device and modify camera preview position based on your screen resolution.

To start the interface simply use this command

```bash
mirror
```

(Still WIP) as of yet installer doesn't add magic mirror software to autostart, you'll have to do this manually.

## Donations
If you like it feel free to donate, every little helps

<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="8E6LS9N72ACYE">
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>

## Contribution
You are free to modify and improve this software. If you spot any bugs feel free to submit any bugs you find into the issue box. If your feeling extra brave, you can fork repository and try to fix some of the bugs yourself and submit a pull request.

## Authors

Developed by [Fedor Bobylev](https://techblogogy.github.io), [Tanya Batsenko](https://www.facebook.com/tanya.batsenko), [Zhenya Kravchenko](https://www.facebook.com/profile.php?id=100003291290867)
