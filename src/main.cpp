#include <cstdlib>
#include <iostream>
#include <filesystem>
#include <array>
#include <vector>
#include <cassert>
#include "../include/compare.hpp"
#include "../include/dirs.hpp"

#define FIRST_ARGUMENT 1
#define SECOND_ARGUMENT 2
#define TOTAL_ARGUMENTS 3 

namespace fs = std::filesystem; 
// checks for number of arguments, path type and returns the valid argumnent.
std::vector<fs::path> valid_args(char* argv[], int arg_count) {
    if (arg_count != TOTAL_ARGUMENTS) {
        std::cerr << "Check the command line arguments" << std::endl;  
        exit(EXIT_FAILURE);
    } 

    if(!fs::exists(argv[FIRST_ARGUMENT])) {
        std::cerr << "The source directory does not exist" << std::endl;  
        exit(EXIT_FAILURE);
    }

    // The source should exist. 
    // The destination can exist or not exist. 
    std::vector<fs::path> vector_valid_args; 
    vector_valid_args.push_back(argv[FIRST_ARGUMENT]); 
    vector_valid_args.push_back(argv[SECOND_ARGUMENT]); 
    return vector_valid_args; 
}


int main(int arg_count, char* argv[]) {
    std::vector<std::filesystem::path> v_cmdLineArgs; 
    std::vector<fs::path> args_vector = valid_args(argv, arg_count);
    // so make tree will possibly be called from here. 

    file_tree src = file_tree(); 
    src.make_tree(args_vector[0]); 

    file_tree dest = file_tree(); 
    dest.make_tree(args_vector[1]); 

    src.show(); 
    dest.show(); 



    return 0; 
}
