namespace projetorpg.src.Entities
{
    public class Wizard : Hero
    {
        public Wizard(string name, int level, string herotype) : base(name, level, herotype)
        {
            this.Name=name;
            this.Level=level;
            this.Herotype=herotype; 
        }
       
        public override string Attack() 
        {
            return this.Name + " Lançou Magia! "; 
        }
        public string Attack(int Bonus)
        {
            if (Bonus > 6)
            {
                return this.Name + " lançou magia super efetiva com bônus de " + Bonus;   
            }
            else
            {
                return this.Name +" lançou magia com força fraca com bônus de " + Bonus;              
            }

        }
    }    
}