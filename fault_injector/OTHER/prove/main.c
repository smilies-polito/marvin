#include <stdio.h>
#include <stdlib.h>

int main() {
    // Path to the Python program to be executed
    const char *python_program = "program1.py";

    // Build the command to run the Python program
    char command[256];
    snprintf(command, sizeof(command), "python %s", python_program);

    // Open a pipe to read the output of the Python program
    FILE *pipe = popen(command, "r");
    if (pipe == NULL) {
        perror("popen");
        return EXIT_FAILURE;
    }

    // Read and print the output from the Python program in real time
    char buffer[128];
    while (fgets(buffer, sizeof(buffer), pipe) != NULL) {
        printf("%s", buffer);
        fflush(stdout); // Ensure immediate printing
    }

    // Close the pipe and get the return code of the Python program
    int return_code = pclose(pipe);
    if (return_code == -1) {
        perror("pclose");
        return EXIT_FAILURE;
    }

    // Print the exit status of the Python program
    if (WIFEXITED(return_code)) {
        printf("\nPython program exited with status: %d\n", WEXITSTATUS(return_code));
    } else {
        printf("\nPython program terminated abnormally.\n");
    }

    return EXIT_SUCCESS;
}
