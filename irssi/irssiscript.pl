use Irssi;
#use strict;
use warnings;
$VERSION = '1.00';
% IRSSI = (
    authors => 'Ravinder Singh',
    contact => 'n30.2006@gmail.com',
    name => 'Nickserv script',
    description => 'Foobar',
    license => 'Public Domain'
);
$count = 0;

$mynick = 
$mypass =

sub nickserv
{
    my @servers = Irssi::servers();
    for my $s (@servers)
    {
        Irssi::print($s->{tag});
    }
}

sub nickserv_notice
{
    my ($server, $data, $nick, $address) = @_;
    my ($target, $text) = $data =~ /^(\S*)\s:(.*)/;
    Irssi::print($data);
    Irssi::print($target . "--->" . $text);
    if ($address && $address eq 'services@ircservices.blinkenshell.org' )
    {
        if ($text eq 'please choose a different nick.')
        {
            $server->command("MSG NickServ IDENTIFY $mynick $mypass");
            #Irssi::print("Sent IDENTIFY message to NickServ");
        } elsif ($text eq 'Your nickname is not registered. To register it, use: /msg NickServ REGISTER password email')
        {
            $server->command("MSG NickServ RECOVER $mynick $mypass");
            #Irssi::print("Sent RECOVER message to NickServ");
        }
    }       
}

sub getservers2
{
    $s->print("foo");
}

Irssi::command_bind('NS', 'nickserv');
Irssi::signal_add('event notice', 'nickserv_notice');
    
