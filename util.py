import xml.etree.ElementTree as ET
from datetime import datetime
from datetime import timedelta

from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np


def _read_xml_dataframe(file):
    tree = ET.parse(file)
    root = tree.getroot()
    data = [child.attrib for child in root]
    df = pd.DataFrame(data)
    df["Id"] = df["Id"].apply(pd.to_numeric)
    df.set_index("Id", inplace=True)
    return df


def read_tags():
    df = _read_xml_dataframe('data/Tags.xml')
    df["Count"] = df["Count"].apply(pd.to_numeric)
    df["ExcerptPostId"] = df["ExcerptPostId"].apply(pd.to_numeric)
    df["WikiPostId"] = df["WikiPostId"].apply(pd.to_numeric)
    return df


def read_users():
    df = _read_xml_dataframe('data/Users.xml')
    df["Reputation"] = df["Reputation"].apply(pd.to_numeric)
    df["Views"] = df["Views"].apply(pd.to_numeric)
    df["UpVotes"] = df["UpVotes"].apply(pd.to_numeric)
    df["DownVotes"] = df["DownVotes"].apply(pd.to_numeric)
    df["AccountId"] = df["AccountId"].apply(pd.to_numeric)
    df["CreationDate"] = df["CreationDate"].apply(pd.to_datetime)
    df["LastAccessDate"] = df["LastAccessDate"].apply(pd.to_datetime)
    return df


def read_posts():
    df = _read_xml_dataframe('data/Posts.xml')

    def _remove_html_tags(x):
        return BeautifulSoup(x, "lxml").get_text()

    def _to_timestamp(x):
        if x is np.nan:
            return x
        return (int)(pd.to_datetime(x).to_pydatetime().timestamp())

    df["Body"] = df["Body"].apply(_remove_html_tags)
    df["AcceptedAnswerId"] = df["AcceptedAnswerId"].apply(pd.to_numeric)
    df["AnswerCount"] = df["AnswerCount"].apply(pd.to_numeric)
    df["CommentCount"] = df["CommentCount"].apply(pd.to_numeric)
    df["FavoriteCount"] = df["FavoriteCount"].apply(pd.to_numeric)
    df["LastEditorUserId"] = df["LastEditorUserId"].apply(pd.to_numeric)
    df["OwnerUserId"] = df["OwnerUserId"].apply(pd.to_numeric)
    df["ParentId"] = df["ParentId"].apply(pd.to_numeric)
    df["PostTypeId"] = df["PostTypeId"].apply(pd.to_numeric)
    df["Score"] = df["Score"].apply(pd.to_numeric)
    df["ViewCount"] = df["ViewCount"].apply(pd.to_numeric)
    df["LastActivityDate"] = df["LastActivityDate"].apply(_to_timestamp)
    df["CreationDate"] = df["CreationDate"].apply(_to_timestamp)
    df["CommunityOwnedDate"] = df["CommunityOwnedDate"].apply(_to_timestamp)
    df["ClosedDate"] = df["ClosedDate"].apply(_to_timestamp)
    return df


def read_post_history():
    return _read_xml_dataframe('data/PostHistory.xml')


def read_votes():
    return _read_xml_dataframe('data/Votes.xml')


def read_post_links():
    return _read_xml_dataframe('data/PostLinks.xml')


def read_comments():
    return _read_xml_dataframe('data/Comments.xml')


def read_badges():
    return _read_xml_dataframe('data/Badges.xml')


def extract_tags(tags_string):
    pattern = re.compile('<(.*?)>')
    return pattern.findall(tags_string)


def add_months(d, n=1):
    return (datetime.fromtimestamp(d)+timedelta(n*365/12)).timestamp()


if __name__ == '__main__':
    posts_df = read_posts()
    add_months(posts_df["CreationDate"].values[0], 3)
    pass
