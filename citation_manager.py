#! /usr/bin/env python3
from crossref.restful import Works
import pprint

input_doi = "10.1038/nbt.2514"
works = Works()
paper = works.doi(input_doi)
pp    = pprint.PrettyPrinter(indent=4)
pp.pprint(paper)