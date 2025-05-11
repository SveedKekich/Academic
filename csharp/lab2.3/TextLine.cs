public class TextLine : IRegister
{
    private string content;

    public TextLine(string text)
    {
        content = text;
    }

    public string Content => content;

    public void ToUpper()
    {
        content = content.ToUpper();
    }
}
