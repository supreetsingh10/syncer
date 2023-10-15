#include "../include/dirs.hpp"
#include <filesystem>
#include <iostream>
#include <memory>
#include <memory_resource>
#include <pstl/glue_execution_defs.h>
#include <queue>
#include <algorithm>

namespace fs = std::filesystem; 
using de = fs::directory_entry; 

file_tree::file_tree(): parent_dir_node(nullptr) {
} 

file_tree::~file_tree() {
}


void file_tree::make_tree(const fs::path& dir_path) {
    std::queue<dir_node*> sub_dir_traverse_q; 
    de d(dir_path); 
    dir_node* temp = nullptr; 
    // first directory
    if(d.is_directory()) {
        parent_dir_node = new dir_node(); 
        parent_dir_node->dir_path = dir_path;
        temp = parent_dir_node; 
        // loop_queue.push(d); 
    }

    while (temp) {
       for(const auto di : fs::directory_iterator(de(temp->dir_path))) {
           if(di.is_directory()) {
              // making a new node for the sub_directory
              dir_node *sub_temp = new dir_node(); 
              sub_temp->dir_path = di.path();
              // pushing the subdir to the parent directory vector
              temp->sub_dirs.push_back(sub_temp); 
              sub_dir_traverse_q.push(sub_temp); 
           } else {
              temp->files.push_back(di.path()); 
           }
       }

       if(sub_dir_traverse_q.size() != 0) {
           temp = sub_dir_traverse_q.front(); 
           sub_dir_traverse_q.pop(); 
       } else {
          break;  
       }
    }

}


void file_tree::show() {
    if(!parent_dir_node)
        return; 

    dir_node *temp = parent_dir_node; 
    std::queue<dir_node*> sub_dir_traverse_q; 

    while(temp) {
       std::cout << temp->dir_path << std::endl; 
       for(const auto sd : temp->sub_dirs) {
           sub_dir_traverse_q.push(sd); 
       } 

      temp = sub_dir_traverse_q.front();  
      sub_dir_traverse_q.pop(); 
    }
}


const dir_node* file_tree::get_parent_node() const {
    return parent_dir_node;
}
