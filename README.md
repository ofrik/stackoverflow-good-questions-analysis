# stackoverflow-good-questions-analysis
We plan to analyze what's making a good/bad question/answer in stackoverflow. Try to come up with features that correlate with high probability of highly/low ranked questions/answers.
<!-- We plan to create few features to the how much the subject of the topic is new and going to be trendy by using labeled topic modeling in order to evaluate the trend potential of a post, create a rating for how major each user in defining and leading new trends and combine these using machine learning to determine new trends. -->

# TODO's Text Analysis
- [x] Check the score distribution of questions and define highly/low ranked questions threshold.
- [x] Check the score distribution of answers and define highly/low ranked answers threshold.
- [x] Label questions for high/low/regular
- [x] Label answers for high/low/regular
- [ ] Extract structural features from the questions/answers such as:
- - [ ] length
- - [ ] POS frequency (for text only)
- - [ ] number of links
- - [ ] code / text ratio
- - [ ] number of comments?
For answers only:
- - [ ] question / answer length ratio
- - [ ] question /answer code ratio
- - [ ] question - answer time difference
- [ ] Extract more complicated features such as:
- - [ ] tf-idf
- - [ ] topics correlation (via topic modeling)
- [ ] Train a regression model to predict the score of question/answer

Note: I think the model will perform better if we will split the questions from the answers in the training as i don't think a good question features will work well for answer.

# TODO's Network Analysis

