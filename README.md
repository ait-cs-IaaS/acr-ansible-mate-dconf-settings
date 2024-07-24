# Ansible-Role: acr-ansible-mate-dconf-settings

AIT-CyberRange: Customizes ubuntu mate desktop environment.


## Requirements

- Debian or Ubuntu 

## Role Variables

**Example config:**

```yaml
client_dconf_settings:
  /org/mate/panel/general/default-layout: familiar
  /desktop/ibus/panel/custom-font: Ubuntu 10
  /org/mate/caja/desktop/font: Ubuntu 10
  /org/mate/mate-menu/applet-text: menu
  /org/mate/panel/objects/clock/prefs/show-date: true
  /org/mate/panel/objects/clock/prefs/show-seconds: true
  /org/mate/desktop/interface/buttons-have-icons: false
  /org/mate/desktop/interface/document-font-name: Ubuntu 10
  /org/mate/desktop/interface/font-name: Ubuntu 10
  /org/mate/desktop/interface/gtk-theme: Yaru-bark-dark
  /org/mate/desktop/interface/icon-theme: Yaru-bark-dark
  /org/mate/desktop/interface/menus-have-icons: false
  /org/mate/desktop/interface/enable-animations: false
  /org/mate/desktop/interface/gtk-enable-animations: false
  /org/mate/marco/general/theme: Spidey-Left
  /org/mate/marco/general/titlebar-font: Ubuntu Medium 10
  /org/mate/power-manager/sleep-computer-ac: 0
  /org/mate/power-manager/sleep-display-ac: 0
  /org/mate/screensaver/idle-activation-enabled: false
```

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - acr-ansible-mate-dconf-settings
```

## License

GPL-3.0

## Author

- Lenhard Reuter