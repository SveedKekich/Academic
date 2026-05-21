using MessengerApi.Data;
using MessengerApi.Models;
using Microsoft.EntityFrameworkCore;

namespace MessengerApi.Services;

public class MessageService
{
    private readonly AppDbContext _context;

    public MessageService(AppDbContext context)
    {
        _context = context;
    }

    public async Task<(bool Success, string Error, Message? Message)>
        SendMessage(Guid senderId, Guid receiverId, string text)
    {
        if (string.IsNullOrWhiteSpace(text))
            return (false, "Message cannot be empty", null);

        var senderExists =
            await _context.Users.AnyAsync(x => x.Id == senderId);

        var receiverExists =
            await _context.Users.AnyAsync(x => x.Id == receiverId);

        if (!senderExists || !receiverExists)
            return (false, "User does not exist", null);

        var message = new Message
        {
            SenderId = senderId,
            ReceiverId = receiverId,
            Text = text
        };

        _context.Messages.Add(message);

        await _context.SaveChangesAsync();

        return (true, "", message);
    }

    public async Task<List<Message>> GetHistory(Guid user1, Guid user2)
    {
        return await _context.Messages
            .Where(m =>
                (
                    m.SenderId == user1 &&
                    m.ReceiverId == user2
                )
                ||
                (
                    m.SenderId == user2 &&
                    m.ReceiverId == user1
                )
            )
            .OrderBy(m => m.Timestamp)
            .ToListAsync();
    }

    public async Task<bool> EditMessage(Guid messageId, string newText)
    {
        var message =
            await _context.Messages.FindAsync(messageId);

        if (message == null)
            return false;

        if (message.DeletedForEveryone)
            return false;

        message.Text = newText;
        message.IsEdited = true;

        await _context.SaveChangesAsync();

        return true;
    }

    public async Task<bool> DeleteForEveryone(Guid messageId)
    {
        var message =
            await _context.Messages.FindAsync(messageId);

        if (message == null)
            return false;

        message.DeletedForEveryone = true;

        await _context.SaveChangesAsync();

        return true;
    }

    public async Task<bool> DeleteForMe(Guid messageId, Guid userId)
    {
        var message =
            await _context.Messages.FindAsync(messageId);

        if (message == null)
            return false;

        if (message.SenderId == userId)
            message.DeletedForSender = true;

        if (message.ReceiverId == userId)
            message.DeletedForReceiver = true;

        await _context.SaveChangesAsync();

        return true;
    }
}