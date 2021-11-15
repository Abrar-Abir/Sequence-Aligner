# Sequence Aligner
## A Python project for global alignment of Nucleic Acid sequences using FOGSAA
---
### Project Description: 
In bioinformatics, a sequence alignment is a way of arranging the sequences of DNA, RNA, or protein to identify regions of similarity that may be a consequence of functional, structural, or evolutionary relationships between the sequences.[1] Aligned sequences of nucleotide or amino acid residues are typically represented as rows within a matrix. Gaps are inserted between the residues so that identical or similar characters are aligned in successive columns. [[1](https://en.wikipedia.org/wiki/Sequence_alignment)]
This project will cover **[pairwaise](https://en.wikipedia.org/wiki/Sequence_alignment#Pairwise_alignment) [global](https://en.wikipedia.org/wiki/Sequence_alignment#Global_and_local_alignments) alignment** of DNA/RNA sequences.

### Competitive Analysis: 
There are many softwares for [Databese Search](https://en.wikipedia.org/wiki/List_of_sequence_alignment_software#Database_search_only), [Pairwaise Alignment](https://en.wikipedia.org/wiki/List_of_sequence_alignment_software#Pairwise_alignment), [Genomics Analysis](https://en.wikipedia.org/wiki/List_of_sequence_alignment_software#Genomics_analysis), and [Alignment Visualization](https://en.wikipedia.org/wiki/List_of_alignment_visualization_software) which uses sequence alignment for analysis.
This project will implement the principle of sequence alignment from scratch- for `pairwaise global alignment` of DNA/RNA sequences

### Structural Plan: 
A structural plan for how the finalized project will be organized in different functions, files and/or objects.

* Graphical User Interface (gui.py) | Prompt for uploading the sequences to be aligned
* Back-end for Alignment (fogsaa.py) | FOGSAA Algorithm
* Graphical User Interface (gui.py) | Displaying the aligned sequence

### Algorithmic Plan: 
There are many algorithms developed for sequence alignment, namely- [Needleman–Wunsch (NW) algorithm](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm), [Global Alignment Program Version 3 (GAP3)](https://academic.oup.com/bioinformatics/article/19/2/228/372697), [FOGSAA (Fast Optimal Global Sequence Alignment Algorithm)](https://www.nature.com/articles/srep01746), etc.
Among them, [FOGSAA (Fast Optimal Global Sequence Alignment Algorithm)](https://www.nature.com/articles/srep01746) is the most efficient and accurate algorithm, and hence this algorithm will be used for this project. 

### Timeline Plan: 
* 15/11/2021 : tp1
* 18/11/2021 : Back-end (Algorithm)
* 20/11/2021 : Front-end (Graphical User Interface)
* 22/11/2021 : MVP (Minimal Viable Project)
* 24/11/2021 : Adding additional algorithm, features
* 26/11/2021 : Final Project

### Version Control Plan: 
[Github](https://github.com/Abrar-Abir/Sequence-Aligner)

### Module List: 
* PyGame
