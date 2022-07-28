<h1 align="center">
<img alt="torchspy" src="assets/icon.png">
</h1>

<p align="center">
<strong>torchspy</strong>, an easy-to-use profiling tool for PyTorch projects. 
</p>

### GPU Memory Profiling
```Python
import torch
import torchspy

def main():
    a = 1
    b = torch.ones(500)
    c = a + b
    torch.max(c)

with torchspy.profile_memory():
    main()

# main.py[2]  Memory: 0 B     a = 1
# main.py[3]  Memory: 2 KB    b = torch.ones(500)
# main.py[4]  Memory: 2 KB    c = a + b
# main.py[5]  Memory: 0 B     torch.max(d)
```

### Contributions
- [font-generator.com](https://www.font-generator.com/) for generating the icon