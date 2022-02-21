namespace projetorpg.src.Entities
{
    public abstract class Hero
    {
        public string Name {get; set;}
        public int Level {get; set;}
        public string Herotype {get; set;}
    public Hero(string name, int level, string herotype)

        {
            this.Name=name;
            this.Level=level;
            this.Herotype=herotype;  
        }
        public override string ToString()
        {
            return $@"
            {this.Name} 
            {this.Level} 
            {this.Herotype}";
        }
        public virtual string Attack() 
        {
            return this.Name + " atacou com sua espada ! "; 


        }
   
    }


}