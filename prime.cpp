#include <iostream>
#include <vector>
#include <cmath>
#include <thread>
#include <mutex>
#include <atomic>
#include <chrono>

std::mutex io_mutex;

bool is_prime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i <= std::sqrt(n); i += 2)
        if (n % i == 0)
            return false;
    return true;
}

void find_primes(int start, int step) {
    for (int i = start; true; i += step) {
        if (is_prime(i)) {
            std::lock_guard<std::mutex> lock(io_mutex);
            std::cout << i << std::endl;
        }
    }
}

int main() {
    int thread_count = std::thread::hardware_concurrency(); // Number of threads to run
    std::vector<std::thread> threads;

    // Launch threads
    for (int i = 0; i < thread_count; ++i) {
        threads.emplace_back(find_primes, 2 + i, thread_count);
    }

    // Threads will run indefinitely. To stop, press Ctrl+C in the terminal.
    for (auto &thread : threads) {
        if (thread.joinable()) {
            thread.join();
        }
    }

    return 0;
}