using GameSimulation.Domain;
using GameSimulation.Domain.Models;

namespace GameSimulation.Patterns.State
{
    public interface IGameState
    {
        void Install(Game context, Device device);
        void Launch(Game context, Device device);
        void Login(Game context);
        void Save(Game context);
        void Load(Game context);
        void Close(Game context);
    }
}