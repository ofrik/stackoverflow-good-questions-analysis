import xml.etree.ElementTree as ET
import pandas as pd

def _read_xml_dataframe(file):
    tree = ET.parse(file)
    root = tree.getroot()
    data = [child.attrib for child in root]
    df = pd.DataFrame(data)
    return df

def read_tags():
    return _read_xml_dataframe('data/Tags.xml')


def read_users():
    return _read_xml_dataframe('data/Users.xml')


def read_posts():
    return _read_xml_dataframe('data/Posts.xml')


def read_post_history():
    return _read_xml_dataframe('data/PostHistory.xml')


def read_votes():
    return _read_xml_dataframe('data/Votes.xml')


def read_users():
    return _read_xml_dataframe('data/Users.xml')


def read_post_links():
    return _read_xml_dataframe('data/PostLinks.xml')


def read_comments():
    return _read_xml_dataframe('data/Comments.xml')


def read_badges():
    return _read_xml_dataframe('data/Badges.xml')


if __name__ == '__main__':
    read_tags()
    pass
