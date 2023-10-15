#pragma once
#include <filesystem>
#include <queue>
#include <memory>
#include <set>
#include <string>
#include <iterator>
#include <vector>


// Datastructure 
// Independent of path names. 
// uses folder names in that come in the way 
// It will form a tree which will have Directories as it's nodes. Everything else which is not a directory will be in the another vector. 

struct dir_node {
    std::filesystem::path dir_path; 
    std::vector<std::filesystem::path> files;
    std::vector<dir_node*> sub_dirs; 
}; 

class file_tree {
    public: 
        file_tree(); 
        virtual ~file_tree(); 
        void make_tree(const std::filesystem::path& dir_path); 

        void show(); 
        void sort_file_vector() const; 

        std::filesystem::path arg_path; 
        const dir_node* get_parent_node() const; 
    private: 
        // this will store the sub directories in the given directory. 
        // this should be allocated on the heap. 
        // std::unique_ptr<std::queue<std::filesystem::path>> dire_path_queue; 
        dir_node* parent_dir_node; 
        std::vector<dir_node*> vec_sub_dirs; 
}; 
