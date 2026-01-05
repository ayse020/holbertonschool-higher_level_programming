import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    
    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The name of the file to save the XML to
    
    Returns:
        None
    """
    try:
        # Create the root element
        root = ET.Element("data")
        
        # Add each dictionary item as a child element
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        
        # Create ElementTree and write to file
        tree = ET.ElementTree(root)
        
        # Use UTF-8 encoding and add XML declaration
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        
    except Exception as e:
        print(f"Error during serialization: {e}")
        raise


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.
    
    Args:
        filename (str): The name of the XML file to read
    
    Returns:
        dict: The deserialized dictionary, or an empty dict if error occurs
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary from XML elements
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text
        
        return result_dict
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return {}
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return {}
    except Exception as e:
        print(f"Error during deserialization: {e}")
        return {}
