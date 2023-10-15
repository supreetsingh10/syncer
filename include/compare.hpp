#pragma once
#include <filesystem>
#include "../include/dirs.hpp"

class file_tree; 
enum file_changes {
    ADDED,
    REMOVED,
    UPDATED,
}; 

class compare_trees {
    public: 
        compare_trees(file_tree* s, file_tree *dt); 
        virtual ~compare_trees(); 

        void compare_with_name(); 
        void compare_with_sub_dirs_only(); 
    private: 
        file_tree *src_tree, *dest_tree; 
        // Have common unchanged files 
        // Have the names of changed files in when compared to dest
        // Have the name of deleted files in when compared to dest
}; 
