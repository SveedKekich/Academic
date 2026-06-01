using System;

namespace GameSimulator
{
    public class GameEventArgs : EventArgs
    {
        public string Message { get; set; }
        public GameEventArgs(string message) => Message = message;
    }
}