/*
10001st prime
https://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
*/

// I've found 10001st prime by this c# console programme just in 2 miliseconds! (2/1000 sec)

using System;
using System.Collections.Generic;

namespace Eratosten_CS_SpeededUp
{
    class Program
    {
        static void Main()
        {
			int kacaKadar = 1000000;
			bool[] sayi = new bool[kacaKadar];
			sayi[2] = true;
			List<int> asal = new List<int>();
			asal.Add(2);
			int say = 0;
			for (int x = 3; x < kacaKadar-2; x += 2)
			{
				if (!sayi[x])
				{
					asal.Add(x);
					say += 1;
                    if (say == 10001)
                    {
						break;
                    }
					for (int y = x * 2; y < kacaKadar-2; y += x)
					{
						sayi[y] = true;
					}
				}
			}

			Console.WriteLine(asal[10000].ToString());
			Console.Beep();
			Console.ReadKey();
		}
    }
}