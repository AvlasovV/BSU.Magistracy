#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <unordered_map>
#include <queue>

using namespace std;


const int ALPHABET_SIZE = 26;

struct TreeNode {
	char symbol;
	TreeNode *children[ALPHABET_SIZE];
	TreeNode *parent;
	TreeNode *link = NULL;
	TreeNode *term_link;
	int max_seq = 0;
	bool terminal = false;

};


class Tree {
	TreeNode *root;

public:

	Tree(int alph_size = ALPHABET_SIZE) {
		root = new TreeNode;
		root->parent = root;
		root->link = root;
		root->symbol = -1;
		//memset(root->children, NULL, sizeof(TreeNode) * alph_size);
		for (size_t i = 0; i < alph_size; i++)
		{
			root->children[i] = NULL;
		}
	}
	
	TreeNode *get_node(TreeNode* parent, char c, int alph_size = ALPHABET_SIZE)	{
		TreeNode *pointer = new TreeNode;
		
		pointer->symbol = c;
		pointer->terminal = false;
		pointer->parent = parent;
		//memset(pointer->children, NULL, sizeof(TreeNode) * alph_size);
		for (size_t i = 0; i < alph_size; i++)
		{
			pointer->children[i] = NULL;
		}

		return pointer;
	}

	void add_string(const string &s, int alph_size = 26) {
		TreeNode * buf = root;
		for (size_t i = 0; i < s.size(); i++)
		{
			char c = s[i] - 'a';
			if (!buf->children[c]) {
				buf->children[c] = this->get_node(buf, c);
			}
			//buf->symbol = c;
			//buf->children[c]->parent = buf;

			buf = buf->children[c];
		}
		buf->terminal = true;
	}

	int find_suffix_strings_and_longest_sequence() {
		queue<TreeNode*> q;
		q.push(root);
		TreeNode * buf;
		TreeNode *suf_link;
		int longest_seq = 0;
		while (!q.empty()) {
			
			buf = q.front();
			q.pop();
			
			
			for (size_t i = 0; i < ALPHABET_SIZE; i++)
			{
				//if (buf->children[i] != NULL) {
				if (buf->children[i]) {
					q.push(buf->children[i]);
				}
			}

			suf_link = buf->parent->link;
			
			while (suf_link != root) {
				if (suf_link->children[buf->symbol]) {
					suf_link = suf_link->children[buf->symbol];
					break;
				}
				suf_link = suf_link->link;
			}
			if ((suf_link == root) && (buf->symbol != -1) && (suf_link->children[buf->symbol]) && (buf->parent != root)) // GOVNOKOD, KSTA
					suf_link = suf_link->children[buf->symbol];

			buf->link = suf_link;

			
			buf->max_seq = max(buf->parent->max_seq, buf->link->max_seq);

			if (buf->terminal)
				buf->max_seq++;
			
			if (longest_seq < buf->max_seq)
				longest_seq = buf->max_seq;

		}
		return longest_seq;
	}
};

void main() {
	ifstream input_file;
	input_file.open("input.txt");

	string str;
	int n, max_seq;
	Tree tree = Tree();
	
	getline(input_file, str);
	n = stoi(str);

	
	for (size_t i = 0; i < n; i++)
	{
		getline(input_file, str);
		tree.add_string(str);
	}

	input_file.close();

	max_seq = tree.find_suffix_strings_and_longest_sequence();

	ofstream output_file;
	output_file.open("output.txt");

	output_file << max_seq;

	output_file.close();

	//cin.get();
}