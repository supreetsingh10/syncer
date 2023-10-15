#include "../include/compare.hpp"
#include <algorithm>
#include <iostream>
#include <queue>

namespace fs = std::filesystem; 

compare_trees::compare_trees(file_tree* src, file_tree *dest): src_tree(src), dest_tree(dest) {}

compare_trees::~compare_trees() {}

// The entire destination is empty 
// The files need to be updated, deleted and added. 

void compare_trees::compare_with_sub_dirs_only() {
    const dir_node *src_temp, *dest_temp; 
    src_temp = src_tree->get_parent_node(); 
    dest_temp = dest_tree->get_parent_node(); 
    std::queue<dir_node*> src_temp_q, dest_temp_q; 

    while(src_temp) {
        for(const auto di : fs::directory_iterator(fs::directory_entry(src_temp->dir_path))) {

        
        }
    }
}
