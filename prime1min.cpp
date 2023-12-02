#include <iostream>
#include <vector>
#include <cmath>
#include <thread>
#include <mutex>
#include <atomic>
#include <chrono>

std::mutex io_mutex;
std::atomic<bool> stop_flag(false);

bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

// Removed the max_count parameter to ensure continuous operation
void find_primes(int start, int step) {
    for (int i = start; !stop_flag; i += step) {
        if (is_prime(i)) {
            std::lock_guard<std::mutex> lock(io_mutex);
            std::cout << i << std::endl;
            std::cout.flush(); // Flush the output buffer after each prime is printed
        }
    }
}

int main() {
    int thread_count = std::thread::hardware_concurrency(); // Number of threads to run
    std::vector<std::thread> threads;

    auto start_time = std::chrono::high_resolution_clock::now();

    // Launch threads without max_count, they will check for primes continuously
    for (int i = 0; i < thread_count; ++i) {
        threads.emplace_back(find_primes, 2 + i, thread_count);
    }

    // Let them run for 60 seconds
    std::this_thread::sleep_for(std::chrono::seconds(60));
    stop_flag = true; // Signal the threads to stop

    // Join threads
    for (auto &thread : threads) {
        if (thread.joinable()) {
            thread.join();
        }
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;
    std::cout << "Calculated in " << elapsed.count() << " seconds.\n";

    return 0;
}