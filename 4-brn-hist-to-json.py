import aiml
import json

# Load the AIML brain file
kernel = aiml.Kernel()
kernel.loadBrain("bot_brain.brn")




def pattern_mgr_to_json(pattern_mgr):
    def recursive_dict(node):
        result = {}
        for key, value in node.items():
            if isinstance(value, dict):
                result[key] = recursive_dict(value)
            else:
                result[key] = value
        return result

    return recursive_dict(pattern_mgr._root)

# Assuming `pattern_mgr` is an instance of PatternMgr
json_data = pattern_mgr_to_json(kernel._brain)

# Save the JSON data to a file
with open("pattern_mgr.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)






# Save the JSON data to a file
with open("bot_brain.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)
