#!/usr/bin/python3
"""
This module provides functions to serialize and deserialize Python dictionaries
using XML format.

It allows saving dictionary data into an XML file and restoring it back into a
dictionary structure.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary and saves it as an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML file to save the data to.
    """
    # Ensure the input is a dictionary
    data = dictionary

    # Create the root element for the XML
    root = ET.Element("data")
    # Iterate through the dictionary and create XML elements
    for key, value in data.items():
        # Create a sub-element for each key-value pair
        ET.SubElement(root, key).text = value

    # Create an ElementTree object and write it to the file
    tree = ET.ElementTree(root)
    # Write the XML tree to the specified file
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads an XML file and deserializes its content into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: A dictionary reconstructed from the XML content.
    """
    # Parse the XML file and get the root element
    tree = ET.parse(filename)
    # Get the root element of the XML tree
    root = tree.getroot()
    # Create a new dictionary to hold the deserialized data
    new_dict = {}
    # Iterate through the child elements of the root
    for child in root:
        # For each child element, add its tag and text to the dictionary
        new_dict[child.tag] = child.text
    # Return the reconstructed dictionary
    return new_dict
