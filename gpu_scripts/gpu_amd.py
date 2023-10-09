import torch

# Check if a GPU is available; if not, use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Create tensors on the GPU
a = torch.randn(3, 3).to(device)
b = torch.randn(3, 3).to(device)

# Perform a simple calculation on the GPU
result = a + b

# Move the result back to the CPU if needed (for printing, etc.)
result_cpu = result.to("cpu")

# Print the result
print("Result on GPU:")
print(result)
print("\nResult on CPU:")
print(result_cpu)
