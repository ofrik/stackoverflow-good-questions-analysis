# stackoverflow-trends
We plan to create few features to the how much the subject of the topic is new and going to be trendy by using labeled topic modeling in order to evaluate the trend potential of a post, create a rating for how major each user in defining and leading new trends and combine these using machine learning to determine new trends.

# TODO's
- [ ] define a metric for labeling a post/tag new that will become trendy.
- [ ] label the posts for potential trendy & not trendy.
- [ ] clean posts content and create BOW from it.
- [ ] train labeled topic modeling using the posts BOW and their labels.
- [ ] define a metric for assessing the weight of a user on the community.
- [ ] define a metric to rate the user trend leading.
- [ ] combine the trendy/not trendy output of the topic modeling with the user data and train model to determine if the post topic going to be trendy.

# Metrics

## Trendy to be tag
If was used less than three months after the first use of the tag,
If the tag existed a year after

## Trendy to be post topic
If the post has tags that are to be trendy

## User community weight
How many views on his posts - x   
Upvote/downvote ratio - y   
Number of posts - z   
for now - (norm(x)+norm(y)+norm(z))/3  

## User trend leadership
Trendy posts ratio relative to himself - x - trendy/not-trendy  
Trendy posts compared to everyone - y - the percentage  
for now - (x+y)/2
