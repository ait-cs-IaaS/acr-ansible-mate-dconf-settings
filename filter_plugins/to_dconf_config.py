from collections import defaultdict


class FilterModule(object):
    def filters(self):
        return {"to_dconf_config": self.to_dconf_config}

    def to_dconf_config(self, config_dict, **kwargs):

        # Ensure the dict is ordered
        ordered_dict = defaultdict(list)
        for key, value in config_dict.items():
            config_key, config_sub_key = key.rsplit("/", 1)
            ordered_dict[config_key].append({config_sub_key: value})

        # Ensure desired output format
        config_string = []
        for key, values in ordered_dict.items():

            # Remove leading "/"
            section = key.split("/", 1)[1]

            # Write new section
            config_string.append(f"\n[{section}]")
            for item in values:
                for sub_key, sub_value in item.items():
                    config_string.append(format_dconf_value(sub_key, sub_value))

        formated_config = "\n".join(config_string)

        return formated_config


def format_dconf_value(key, value):

    if isinstance(value, bool):
        # Convert Bollean to string
        return f"{key}={str(value).lower()}"

    if isinstance(value, int) or isinstance(value, list):
        # Values that cannot have quotes
        return f"{key}={value}"
    else:
        # Ensure values are wrapped with single quotes (')
        return f"{key}='{value}'"
