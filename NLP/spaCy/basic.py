import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')

for token in doc:
    print(f"{token.text:10}{token.pos_:10}{token.dep_:10}")

print(nlp.pipeline)
print(nlp.pipe_names)

doc = nlp(u"Tesla isn't looking looking into startups anymore")

for token in doc:
    print(f"{token.text:10}{token.pos_:10}{token.dep_:10}")