import os
import torch
import torchspy


def main():
    a = 1
    b = torch.ones(500, device=torch.device('cuda:0'))
    c = a + b
    i = 0
    i += 1
    d = torch.flatten(c).detach().clone()
    torch.max(d)


def test_main():
    with torchspy.profile_memory(lambda f: os.path.dirname(__file__) in f):
        main()
