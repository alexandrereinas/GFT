using System;
using projetorpg.src.Entities;
using static System.Console;


namespace projetorpg
{
    class Program
    {
        static void Main(string[] args)
        {
          Knight Arus = new Knight("Arus", 23, "Knight");
          Wizard Wizard = new Wizard("Jennica", 23, "Wizard");
        WriteLine(Arus.Attack()); 
        WriteLine(Wizard.Attack(7));
        }
    }
    
}
  